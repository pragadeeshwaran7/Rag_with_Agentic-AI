import { useState, useEffect } from 'react';
import { getBoards, generatePaper } from '../api/client';
import PaperPreview from '../components/PaperPreview';
import { Sparkles, Loader2, Settings, FileText } from 'lucide-react';

export default function GeneratorPage() {
  const [boards, setBoards] = useState([]);
  const [formData, setFormData] = useState({
    board: 'CBSE',
    subject: 'Science',
    difficulty: 'Medium',
    full_paper: true
  });
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchBoards() {
      try {
        const data = await getBoards();
        setBoards(data);
        if (data.length > 0) {
          setFormData(prev => ({ ...prev, board: data[0].id, subject: data[0].subjects[0] }));
        }
      } catch (err) {
        console.error("Failed to fetch boards", err);
      }
    }
    fetchBoards();
  }, []);

  const selectedBoardObj = boards.find(b => b.id === formData.board);
  const availableSubjects = selectedBoardObj ? selectedBoardObj.subjects : [];

  const handleGenerate = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const res = await generatePaper(formData);
      setResult(res);
    } catch (err) {
      setError(err.response?.data?.detail || "Failed to generate paper. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex-grow flex flex-col md:flex-row gap-8 pb-12">
      {/* Configuration Panel */}
      <div className={`w-full ${result ? 'md:w-1/3' : 'max-w-2xl mx-auto'} transition-all duration-500`}>
        <div className="glass-panel p-8">
          <div className="flex items-center gap-3 mb-8">
            <Settings className="w-6 h-6 text-primary-500" />
            <h2 className="text-2xl font-bold">Configuration</h2>
          </div>
          
          <form onSubmit={handleGenerate} className="space-y-6">
            <div>
              <label className="block text-sm font-medium text-slate-400 mb-2">Select Board</label>
              <select
                className="input-field appearance-none"
                value={formData.board}
                onChange={(e) => {
                  const bId = e.target.value;
                  const bObj = boards.find(b => b.id === bId);
                  setFormData({ ...formData, board: bId, subject: bObj?.subjects[0] || '' });
                }}
              >
                {boards.map(b => (
                  <option key={b.id} value={b.id}>{b.name}</option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-400 mb-2">Subject</label>
              <select
                className="input-field appearance-none"
                value={formData.subject}
                onChange={(e) => setFormData({ ...formData, subject: e.target.value })}
              >
                {availableSubjects.map(s => (
                  <option key={s} value={s}>{s}</option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-400 mb-2">Difficulty Level</label>
              <div className="grid grid-cols-3 gap-3">
                {['Easy', 'Medium', 'Hard'].map(level => (
                  <button
                    type="button"
                    key={level}
                    className={`py-2 rounded-lg border transition-all ${
                      formData.difficulty === level 
                        ? 'bg-primary-500/20 border-primary-500 text-primary-400' 
                        : 'bg-dark-900 border-slate-700 text-slate-400 hover:border-slate-500'
                    }`}
                    onClick={() => setFormData({ ...formData, difficulty: level })}
                  >
                    {level}
                  </button>
                ))}
              </div>
            </div>

            <div className="pt-4">
              <button 
                type="submit" 
                disabled={loading}
                className="btn-primary w-full text-lg"
              >
                {loading ? (
                  <><Loader2 className="w-5 h-5 animate-spin" /> Generating AI Paper...</>
                ) : (
                  <><Sparkles className="w-5 h-5" /> Generate Paper</>
                )}
              </button>
            </div>
            {error && <p className="text-red-400 text-sm mt-4 text-center">{error}</p>}
          </form>
        </div>
      </div>

      {/* Preview Panel */}
      {result && (
        <div className="w-full md:w-2/3 animate-in fade-in slide-in-from-bottom-8 duration-500">
          <div className="glass-panel p-8 min-h-full">
            <div className="flex items-center justify-between mb-6">
              <div className="flex items-center gap-3">
                <FileText className="w-6 h-6 text-primary-500" />
                <h2 className="text-2xl font-bold">Generated Paper</h2>
              </div>
            </div>
            <PaperPreview content={result.paper_content} />
          </div>
        </div>
      )}
    </div>
  );
}
