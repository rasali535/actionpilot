import os
import json
import asyncio
from typing import Dict, List
from agents.featherless import featherless
from dotenv import load_dotenv

load_dotenv()

class BoardroomCouncil:
    def __init__(self):
        self.research_model = os.getenv("RESEARCH_MODEL", "Qwen/Qwen2.5-72B-Instruct")
        self.trading_model = os.getenv("TRADING_MODEL", "deepseek-ai/DeepSeek-V3")
        # Use the trading model or fallback for the CEO role
        self.ceo_model = self.trading_model

    async def get_gc_opinion(self, market_data: str) -> str:
        """General Counsel: DeepSeek-V3 specializes in risk and logical audit."""
        return await featherless.chat(
            model=self.trading_model,
            system_prompt="You are the General Counsel of Vantage-Point. Audit this market state for compliance and hidden risk.",
            user_prompt=f"Market data: {market_data}"
        )

    async def get_macro_opinion(self, ticker: Dict) -> str:
        """Macro Strategist: Qwen 2.5-72B specializes in global trends and volatility."""
        return await featherless.chat(
            model=self.research_model,
            system_prompt="You are the Macro Strategist. Analyze the global trends and volatility for this asset.",
            user_prompt=f"Ticker: {json.dumps(ticker)}"
        )

    async def deliberate(self, ticker: Dict, ohlc: List, pair: str, whipsaw_report: Dict = None) -> Dict:
        """The Boardroom Council Deliberation Workflow via Featherless"""
        whipsaw_context = ""
        if whipsaw_report:
            whipsaw_context = f"""
        [SIGNAL QUALITY & ANTI-WHIPSAW REPORT]:
        - Kaufman's Efficiency Ratio (ER): {whipsaw_report.get('efficiency_ratio')} ({whipsaw_report.get('regime')})
        - Volatility (ATR): {whipsaw_report.get('atr')} ({whipsaw_report.get('pct_volatility')}% of price)
        - Whipsaw Risk Level: {whipsaw_report.get('whipsaw_risk')}
        - Anti-Whipsaw Recommendation: {whipsaw_report.get('action_recommendation')}
        - System Audit Details: {whipsaw_report.get('reason')}
            """

        market_summary = f"Pair: {pair}, Last: {ticker.get('last')}, 24h Change: {ticker.get('change_percent')}%."
        if whipsaw_report:
            market_summary += f" Whipsaw Risk: {whipsaw_report.get('whipsaw_risk')}. Efficiency Ratio: {whipsaw_report.get('efficiency_ratio')}."
        
        # 1. Parallel Research (Featherless)
        gc_task = self.get_gc_opinion(market_summary + f" System Recommendation: {whipsaw_report.get('action_recommendation') if whipsaw_report else 'PROCEED'}")
        macro_task = self.get_macro_opinion(ticker)
        
        gc_view, macro_view = await asyncio.gather(gc_task, macro_task)
        
        # 2. Final CEO Decision (Featherless / Gemini)
        prompt = f"""
        BOARDROOM DELIBERATION for {pair}
        
        [General Counsel Opinion]: {gc_view}
        [Macro Strategist Opinion]: {macro_view}
        {whipsaw_context}
        [Market Data]: {json.dumps(ohlc[:5])}
        
        As CEO, synthesize these views and make a final trade decision.
        
        CRITICAL REBALANCING RULES:
        1. If the Anti-Whipsaw recommendation is FORCE_HOLD or ADVISE_HOLD, you should strongly favor a "HOLD" action to protect treasury capital from high transaction friction and slippage.
        2. Pay close attention to Kaufman's Efficiency Ratio (ER). If ER < 0.3, the market is in a noisy, whipsaw-prone random walk; you should HOLD unless a high-conviction macro event mandates action.
        3. Explain how signal quality (ER) and volatility (ATR) influenced your final decision in the "reasoning" field.

        Return ONLY valid JSON:
        {{
            "action": "BUY" | "SELL" | "HOLD",
            "reasoning": "A concise synthesis of the boardroom's debate, explicitly mentioning how signal quality/ER and whipsaw risk affected your decision.",
            "risk_score": 0-100,
            "confidence": 0-1.0
        }}
        """
        
        # Pulling Gemini 1.5 through the Featherless endpoint
        response_text = await featherless.chat(
            model=self.ceo_model,
            system_prompt="You are the CEO of Vantage-Point Treasury.",
            user_prompt=prompt
        )
        
        # Clean up JSON formatting
        raw_text = response_text.strip()
        if "```json" in raw_text:
            raw_text = raw_text.split("```json")[1].split("```")[0].strip()
            
        try:
            return json.loads(raw_text)
        except:
            # Fallback for parsing errors
            return {
                "action": "HOLD",
                "reasoning": "Synthesis failed or JSON was invalid, defaulting to HOLD for safety.",
                "risk_score": 50,
                "confidence": 0.5
            }

boardroom = BoardroomCouncil()

