import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.PROD ? '' : 'http://localhost:8000',
});

export const getBoards = async () => {
  const response = await api.get('/api/boards');
  return response.data.boards;
};

export const generatePaper = async (data) => {
  const response = await api.post('/api/generate', data);
  return response.data;
};

export default api;
