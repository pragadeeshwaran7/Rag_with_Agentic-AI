import ReactMarkdown from 'react-markdown';
import html2pdf from 'html2pdf.js';
import { Download } from 'lucide-react';
import { useRef } from 'react';

export default function PaperPreview({ content }) {
  const paperRef = useRef(null);

  const handleDownloadPdf = () => {
    const element = paperRef.current;
    const opt = {
      margin:       10,
      filename:     'mock_question_paper.pdf',
      image:        { type: 'jpeg', quality: 0.98 },
      html2canvas:  { scale: 2 },
      jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
    };

    html2pdf().set(opt).from(element).save();
  };

  return (
    <div>
      <div className="flex justify-end mb-4">
        <button 
          onClick={handleDownloadPdf}
          className="flex items-center gap-2 px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg transition-colors border border-slate-700"
        >
          <Download className="w-4 h-4" /> Export as PDF
        </button>
      </div>
      
      <div className="bg-slate-200 p-2 sm:p-8 rounded-xl overflow-hidden shadow-inner">
        <div 
          ref={paperRef}
          className="paper-container prose prose-sm sm:prose-base prose-paper"
        >
          <ReactMarkdown>{content}</ReactMarkdown>
        </div>
      </div>
    </div>
  );
}
