<template>
  <div class="flex flex-col items-center min-h-screen bg-gray-100 p-6">
    <!-- 헤더 -->
    <header class="text-2xl font-semibold text-gray-800 mb-6">요약Talk</header>

    <!-- 입력 영역 -->
    <div class="w-full max-w-lg bg-white p-6 rounded-2xl shadow-lg">
      <label class="block text-gray-700 mb-2">요약할 내용을 선택하세요</label>
      
      <!-- 입력 방식 선택 -->
      <div class="flex gap-2 mb-4">
        <button
          @click="inputMode = 'url'"
          :class="{'bg-blue-500 text-white': inputMode === 'url', 'bg-gray-200': inputMode !== 'url'}"
          class="p-2 rounded-md w-1/2"
        >
          URL 입력
        </button>
        <button
          @click="inputMode = 'text'"
          :class="{'bg-blue-500 text-white': inputMode === 'text', 'bg-gray-200': inputMode !== 'text'}"
          class="p-2 rounded-md w-1/2"
        >
          직접 입력
        </button>
      </div>

      <!-- URL 입력 -->
      <input
        v-if="inputMode === 'url'"
        v-model="inputText"
        class="w-full p-3 border border-gray-300 rounded-md focus:ring focus:ring-blue-400"
        placeholder="요약할 블로그 URL을 입력하세요."
      />

      <!-- 텍스트 입력 -->
      <textarea
        v-if="inputMode === 'text'"
        v-model="inputText"
        class="w-full p-3 border border-gray-300 rounded-md focus:ring focus:ring-blue-400"
        placeholder="요약할 텍스트를 입력하세요."
      ></textarea>

      <!-- 요약 스타일 선택 -->
      <div class="mt-4">
        <label class="block text-gray-700 mb-2">요약 스타일 선택</label>
        <select v-model="summaryStyle" class="w-full p-2 border border-gray-300 rounded-md">
          <option value="short">짧게 요약</option>
          <option value="detailed">핵심 포인트 요약</option>
        </select>
      </div>

      <!-- 요약 버튼 -->
      <button
        @click="summarize"
        :disabled="loading || !inputText"
        class="w-full mt-4 p-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition disabled:bg-gray-400"
      >
        요약하기
      </button>
    </div>

    <!-- AI 요약 진행 애니메이션 -->
    <div v-if="loading" class="mt-6 flex items-center gap-2 text-gray-600">
      <span class="animate-spin h-5 w-5 border-t-2 border-blue-500 rounded-full"></span>
      AI 요약 중...
    </div>

    <!-- 요약 결과 -->
    <div v-if="summary" class="w-full max-w-lg mt-6 p-4 bg-white rounded-xl shadow-lg">
      <h2 class="text-lg font-semibold text-gray-800">요약 결과</h2>

      <!-- 챗 스타일 UI -->
      <div class="mt-3 p-3 bg-gray-100 rounded-md text-gray-700">
        {{ summary }}
      </div>

      <div class="mt-4 flex justify-end gap-2">
        <button @click="toggleSpeech" class="p-2 bg-gray-200 rounded-md hover:bg-gray-300 transition">
          🔊 {{ speaking ? "음성 정지" : "음성 듣기" }}
        </button>
        <button @click="copySummary" class="p-2 bg-gray-200 rounded-md hover:bg-gray-300 transition">
          📋 복사하기
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const inputText = ref("");
const summary = ref("");
const loading = ref(false);
const speaking = ref(false);
const inputMode = ref("url"); // URL 또는 직접 입력 모드
const summaryStyle = ref("short"); // 요약 스타일 선택

const summarize = async () => {
  if (!inputText.value) return;
  loading.value = true;
  
  // 요약 API 호출 (실제 API 연동 필요)
  setTimeout(() => {
    summary.value = summaryStyle.value === "short"
      ? "짧게 요약된 내용입니다. (실제 API 필요)"
      : "핵심 포인트 요약 내용입니다. (실제 API 필요)";
    
    loading.value = false;
  }, 2000);
};

const toggleSpeech = () => {
  if (!summary.value) return;
  const speech = new SpeechSynthesisUtterance(summary.value);
  speech.lang = "ko-KR";

  if (!speaking.value) {
    speechSynthesis.speak(speech);
    speaking.value = true;
    speech.onend = () => speaking.value = false;
  } else {
    speechSynthesis.cancel();
    speaking.value = false;
  }
};

const copySummary = () => {
  navigator.clipboard.writeText(summary.value);
  alert("요약이 복사되었습니다!");
};
</script>

<style scoped>
/* 추가적인 스타일링 */
</style>
