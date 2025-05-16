<template>
  <div class="threads-container">
    <h1>전체 스레드 목록</h1>

    <!-- 카테고리 필터링 -->
    <div class="category-filter">
      <label for="category">카테고리:</label>
      <select id="category" v-model="selectedCategory">
        <option value="전체">전체</option>
        <option v-for="category in categories" :key="category.id" :value="category.name">
          {{ category.name }}
        </option>
      </select>
    </div>

    <!-- 스레드 목록 -->
    <div class="threads-list">
      <div 
        v-for="thread in filteredThreads" 
        :key="thread.id" 
        class="thread-card" 
        @click="goToDetail(thread.id)"
      >
        <h3>{{ thread.title }}</h3>
        <p>{{ thread.content }}</p>
        <p>{{ thread.date }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'

// 전역 상태처럼 사용할 수 있도록
const threads = ref([]) // 사용자 작성으로 생성됨
const categories = ref([
  { id: 1, name: '문학' },
  { id: 2, name: '자기계발' },
  { id: 3, name: '역사' },
  { id: 4, name: '과학' }
])

const selectedCategory = ref('전체')

const router = useRouter()

// 예시: 작성된 스레드를 동적으로 추가하는 함수 (다른 컴포넌트에서 활용 가능)
function addThread(newThread) {
  threads.value.push({
    id: Date.now(),
    ...newThread,
    date: new Date().toLocaleDateString()
  })
}

const filteredThreads = computed(() => {
  if (selectedCategory.value === '전체') {
    return threads.value
  }
  return threads.value.filter(thread => thread.category === selectedCategory.value)
})

const goToDetail = (threadId) => {
  router.push(`/threads/${threadId}`)
}

// 다른 컴포넌트에서 addThread 사용 가능하게 export
defineExpose({ addThread })
</script>

<style scoped>
.threads-container {
  padding: 20px;
}
.category-filter {
  margin-bottom: 20px;
}
.threads-list {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
}
.thread-card {
  border: 1px solid #ccc;
  padding: 15px;
  border-radius: 8px;
  cursor: pointer;
}
.thread-card:hover {
  background-color: #f0f0f0;
}
</style>