// import { AxiosRequestConfig, AxiosResponse } from 'axios'
import axiosInstance from '../plugins/axios'

interface Department {
  id: string
  name: string
}

class DepartmentDataService {
  getAll() {
    return axiosInstance.get<Department, object[]>('/departments')
  }

  get(id: string | number) {
    return axiosInstance.get(`/departments/${id}`)
  }

  create(data: object) {
    return axiosInstance.post(`/departments/`, data)
  }

  updatePatch(id: string | number, data: object) {
    return axiosInstance.patch(`/departments/${id}/`, data)
  }
}

export default new DepartmentDataService()
