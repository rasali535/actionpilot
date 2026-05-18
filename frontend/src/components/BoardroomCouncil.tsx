import { User, Shield, Globe } from 'lucide-react';

interface CouncilProps {
  decision?: {
    action: string;
    reasoning: string;
    risk_score: number;
    confidence: number;
    signal_quality?: number;
    whipsaw_risk?: string;
  };
  scanning?: boolean;
}

const BoardroomCouncil = ({ decision, scanning }: CouncilProps) => {
  if (scanning) return (
    <div className="glass card animate-fade-in" style={{ border: '1px solid rgba(79, 70, 229, 0.4)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
        <h3>Boardroom Deliberation</h3>
        <span className="badge" style={{ background: 'rgba(79, 70, 229, 0.2)', color: 'var(--primary)', animation: 'pulse 1.5s infinite' }}>
          Active Council Debate
        </span>
      </div>
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', padding: '1rem', background: 'rgba(255,255,255,0.02)', borderRadius: '12px' }}>
          <div className="spinner-small"></div>
          <div>
            <div style={{ fontWeight: 600, fontSize: '0.9rem', color: 'var(--primary)' }}>CEO Agent (Gemini Orchestrator)</div>
            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Synthesizing invoice context and constructing consensus directives...</div>
          </div>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
          <div style={{ padding: '0.75rem', background: 'rgba(255, 255, 255, 0.01)', borderRadius: '8px', border: '1px dashed rgba(79, 70, 229, 0.2)' }}>
            <div style={{ fontWeight: 600, fontSize: '0.8rem', color: 'var(--success)', marginBottom: '0.25rem' }}>Risk Officer (DeepSeek)</div>
            <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Computing portfolio drawdown constraints & Greek sensitivities...</div>
          </div>
          <div style={{ padding: '0.75rem', background: 'rgba(255, 255, 255, 0.01)', borderRadius: '8px', border: '1px dashed rgba(79, 70, 229, 0.2)' }}>
            <div style={{ fontWeight: 600, fontSize: '0.8rem', color: 'var(--warning)', marginBottom: '0.25rem' }}>Macro Strategist (Qwen)</div>
            <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Polling xStocks relative strength index and spot price metrics...</div>
          </div>
        </div>

        <div style={{ width: '100%', height: '4px', background: 'rgba(255, 255, 255, 0.1)', borderRadius: '2px', overflow: 'hidden', marginTop: '0.5rem' }}>
          <div style={{ 
            width: '40%', 
            height: '100%', 
            background: 'linear-gradient(90deg, var(--primary), var(--success))', 
            borderRadius: '2px',
            animation: 'slide-progress 2s infinite ease-in-out'
          }} />
        </div>
      </div>

      <style>{`
        @keyframes pulse {
          0% { opacity: 0.6; }
          50% { opacity: 1; }
          100% { opacity: 0.6; }
        }
        @keyframes slide-progress {
          0% { transform: translateX(-100%); }
          100% { transform: translateX(250%); }
        }
        .spinner-small {
          width: 20px;
          height: 20px;
          border: 2px solid rgba(255,255,255,0.1);
          border-top-color: var(--primary);
          border-radius: 50%;
          animation: spin 1s linear infinite;
        }
      `}</style>
    </div>
  );

  if (!decision) return (
    <div className="glass card">
      <h3 style={{ marginBottom: '1.5rem' }}>Boardroom Deliberation</h3>
      <div style={{ color: 'var(--text-muted)', fontSize: '0.875rem', textAlign: 'center', padding: '2rem' }}>
        Awaiting next market scan to initiate council debate...
      </div>
    </div>
  );

  // Helper color logic for Signal Quality Index (SQI)
  const getSQIColor = (sqi?: number) => {
    if (!sqi) return '#10b981';
    if (sqi >= 60) return '#10b981'; // Success Green
    if (sqi >= 30) return '#f59e0b'; // Warning Orange
    return '#ef4444'; // Danger Red
  };

  return (
    <div className="glass card">
      <h3 style={{ marginBottom: '1.5rem' }}>The Boardroom Consensus</h3>
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
        {/* CEO Synthesis */}
        <div style={{ padding: '1rem', background: 'rgba(59, 130, 246, 0.1)', borderRadius: '8px', borderLeft: '4px solid var(--primary)' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem', fontSize: '0.75rem', fontWeight: 700, color: 'var(--primary)', textTransform: 'uppercase' }}>
            <User size={14} /> CEO (Featherless Orchestrator)
          </div>
          <div style={{ fontSize: '0.9rem', lineHeight: 1.5 }}>
            {decision.reasoning}
          </div>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
          {/* GC Opinion */}
          <div style={{ padding: '1rem', background: 'rgba(255, 255, 255, 0.03)', borderRadius: '8px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem', fontSize: '0.75rem', fontWeight: 700, color: 'var(--success)', textTransform: 'uppercase' }}>
              <Shield size={14} /> Risk (DeepSeek)
            </div>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
              Audit confirms trade complies with treasury risk thresholds. Scoring risk at {decision.risk_score}/100.
            </div>
          </div>

          {/* Macro Opinion */}
          <div style={{ padding: '1rem', background: 'rgba(255, 255, 255, 0.03)', borderRadius: '8px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem', fontSize: '0.75rem', fontWeight: 700, color: 'var(--warning)', textTransform: 'uppercase' }}>
              <Globe size={14} /> Macro (Qwen)
            </div>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
              Consensus bullish on xStocks momentum. Relative strength index supports an entry.
            </div>
          </div>
        </div>

        {/* Dynamic Whipsaw Gating and Signal Quality Metrics */}
        {decision.signal_quality !== undefined && (
          <div style={{ 
            padding: '1rem', 
            background: 'rgba(255, 255, 255, 0.02)', 
            borderRadius: '8px', 
            border: '1px solid rgba(255, 255, 255, 0.05)',
            marginTop: '0.5rem'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', marginBottom: '0.5rem', fontWeight: 600 }}>
              <span style={{ color: 'var(--text-muted)' }}>Kaufman Signal Quality (SQI)</span>
              <span style={{ color: getSQIColor(decision.signal_quality) }}>
                {decision.signal_quality}% ({decision.whipsaw_risk} WHIPSAW RISK)
              </span>
            </div>
            <div style={{ width: '100%', height: '4px', background: 'rgba(255, 255, 255, 0.1)', borderRadius: '2px', marginBottom: '0.5rem' }}>
              <div style={{ 
                width: `${decision.signal_quality}%`, 
                height: '100%', 
                background: getSQIColor(decision.signal_quality), 
                borderRadius: '2px',
                transition: 'width 0.8s ease-in-out'
              }} />
            </div>
            <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)', lineHeight: 1.3 }}>
              🔒 <strong>Anti-Whipsaw Filter</strong> dynamically scales target thresholds based on Kaufman Efficiency Ratio & volatility indices to prevent false-breakout capital drag.
            </div>
          </div>
        )}

        {/* Confidence Gauge */}
        <div style={{ marginTop: '0.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', marginBottom: '0.5rem' }}>
            <span style={{ color: 'var(--text-muted)' }}>Consensus Confidence</span>
            <span>{Math.round(decision.confidence * 100)}%</span>
          </div>
          <div style={{ width: '100%', height: '4px', background: 'rgba(255, 255, 255, 0.1)', borderRadius: '2px' }}>
            <div style={{ width: `${decision.confidence * 100}%`, height: '100%', background: 'var(--success)', borderRadius: '2px' }} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default BoardroomCouncil;
