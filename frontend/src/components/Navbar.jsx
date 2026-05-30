import { BookOpen } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav className="fixed top-0 w-full z-50 glass-panel border-b-0 rounded-none bg-dark-900/80">
      <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        <Link to="/" className="flex items-center gap-3 group">
          <div className="p-2 bg-primary-500/20 rounded-xl group-hover:bg-primary-500/30 transition-colors">
            <BookOpen className="w-6 h-6 text-primary-400" />
          </div>
          <span className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-slate-100 to-slate-400">
            PaperGen AI
          </span>
        </Link>
        <div className="hidden md:flex items-center gap-6 text-sm font-medium text-slate-300">
          <a href="#" className="hover:text-primary-400 transition-colors">Documentation</a>
          <a href="#" className="hover:text-primary-400 transition-colors">Pricing</a>
          <button className="px-5 py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-lg transition-colors border border-slate-700">
            Login
          </button>
        </div>
      </div>
    </nav>
  );
}
