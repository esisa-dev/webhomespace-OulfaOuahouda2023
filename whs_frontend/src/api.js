import axios from 'axios';

const BASE_URL = 'http://localhost:5000';

export async function login(username, password) {
  const response = await axios.post(`${BASE_URL}/login`, { username, password });
  return response.data;
}

export async function logout() {
  const response = await axios.post(`${BASE_URL}/logout`);
  return response.data;
}

export async function getDirectoryData(path) {
  const response = await axios.get(`${BASE_URL}/directory`, { params: { path } });
  return response.data;
}

export async function searchFiles(query, path) {
  const response = await axios.get(`${BASE_URL}/search`, { params: { query, path } });
  return response.data;
}

export async function read_file_content(file_path) {
  const response = await axios.get(`${BASE_URL}/file`, { params: { file_path } });
  return response.data;
}

export async function download_file(file_path) {
  const response = await axios.get(`${BASE_URL}/download`, { params: { file_path }, responseType: 'blob' });
  return response.data;
}

export async function get_file_size(file_path) {
  const response = await axios.get(`${BASE_URL}/size`, { params: { file_path } });
  return response.data;
}
