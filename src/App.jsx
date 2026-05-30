import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import GeneratorPage from './pages/GeneratorPage';

function App() {
  return (
    <Router>
      <div className="min-h-screen flex flex-col">
        <Navbar />
        <main className="flex-grow flex flex-col pt-24 px-6 max-w-7xl mx-auto w-full">
          <Routes>
            <Route path="/" element={<GeneratorPage />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
