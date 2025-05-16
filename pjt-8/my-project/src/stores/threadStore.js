import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useThreadStore = defineStore('threadStore', () => {
  const threads = ref([])

  // 초기 로컬스토리지에서 불러오기
  function loadThreads() {
    const stored = localStorage.getItem('threads')
    threads.value = stored ? JSON.parse(stored) : []
  }

  // 쓰레드 저장 및 로컬스토리지 동기화
  function addThread(newThread) {
    threads.value.push({
      id: Date.now(),
      ...newThread,
      date: new Date().toLocaleDateString()
    })
    localStorage.setItem('threads', JSON.stringify(threads.value))
  }

  // ID로 쓰레드 찾기
  function getThreadById(id) {
    return threads.value.find(thread => thread.id === id)
  }

  return {
    threads,
    loadThreads,
    addThread,
    getThreadById
  }
})