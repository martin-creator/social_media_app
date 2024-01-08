<template>
  <main class="min-h-screen flex items-center justify-center bg-gradient-to-r from-indigo-700 to-indigo-500 text-white p-4 md:p-8">
    <div class="text-center">
      <h1 class="text-4xl md:text-6xl font-extrabold mb-4">Welcome to SciNet</h1>
      <p class="text-base md:text-lg mb-8">Connecting scientists worldwide for collaborative research and innovation.</p>
      <div class="flex flex-col md:flex-row justify-center md:space-x-8 mb-8">
        <div class="flex items-center mb-4 md:mb-0">
          <svg class="w-8 h-8 md:w-12 md:h-12 text-indigo-300" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 6V6m0 6h6M12 6H6"></path></svg>
          <span class="ml-2 text-sm md:text-xl font-semibold">Discover research</span>
        </div>
        <div class="flex items-center mb-4 md:mb-0">
          <svg class="w-8 h-8 md:w-12 md:h-12 text-indigo-300" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M12 5l7 7-7 7"></path></svg>
          <span class="ml-2 text-sm md:text-xl font-semibold">Collaborate with experts</span>
        </div>
        <div class="flex items-center">
          <svg class="w-8 h-8 md:w-12 md:h-12 text-indigo-300" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
          <span class="ml-2 text-sm md:text-xl font-semibold">Stay updated on breakthroughs</span>
        </div>
      </div>
      <a href="/login" class="inline-block bg-white text-indigo-700 px-6 md:px-10 py-3 md:py-4 rounded-full font-bold transition duration-300 ease-in-out hover:bg-indigo-700 hover:text-white">Join SciNet</a>
    </div>
  </main>
</template>
