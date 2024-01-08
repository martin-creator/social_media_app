<template>
  <div>
    <!-- Navigation Bar -->
    <nav class="py-4 px-6 md:px-8 border-b border-gray-200">
      <div class="max-w-7xl mx-auto flex items-center justify-between">
        <div class="flex items-center">
          <a href="#" class="text-2xl font-extrabold">SciNet</a>
        </div>

        <!-- Mobile Menu Toggle -->
        <div class="md:hidden">
          <!-- Add a mobile menu toggle button -->
        </div>

        <!-- Center Menu Items -->
        <div class="hidden md:flex space-x-8">
          <RouterLink to="/feed" class="text-purple-700 flex items-center">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5">
              <!-- Feed icon -->
            </svg>
          </RouterLink>

          <RouterLink to="/chat" class="flex items-center">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5">
              <!-- Chat icon -->
            </svg>
          </RouterLink>

          <RouterLink to="/notifications" class="flex items-center">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5">
              <!-- Notifications icon -->
            </svg>
          </RouterLink>

          <RouterLink to="/search" class="flex items-center">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1.5">
              <!-- Search icon -->
            </svg>
          </RouterLink>
        </div>

        <!-- Right Menu Items -->
        <div class="flex items-center">
          <template v-if="userStore.user.isAuthenticated && userStore.user.id">
            <RouterLink :to="{name: 'profile', params:{'id': userStore.user.id}}">
              <img :src="userStore.user.avatar" class="w-10 h-10 rounded-full">
            </RouterLink>
          </template>

          <template v-else>
            <RouterLink to="/login" class="mr-4 py-2 px-4 bg-gray-600 text-white rounded-lg">Log in</RouterLink>
            <RouterLink to="/signup" class="py-2 px-4 bg-purple-600 text-white rounded-lg">Sign up</RouterLink>
          </template>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="px-4 md:px-8 py-6 bg-gray-100">
      <RouterView />
    </main>

    <Toast />
  </div>
</template>


<script>
    import axios from 'axios'
    import Toast from '@/components/Toast.vue'
    import { useUserStore } from '@/stores/user'

    export default {
        setup() {
            const userStore = useUserStore()

            return {
                userStore
            }
        },

        components: {
            Toast
        },

        beforeCreate() {
            this.userStore.initStore()

            const token = this.userStore.user.access

            if (token) {
                axios.defaults.headers.common["Authorization"] = "Bearer " + token;
            } else {
                axios.defaults.headers.common["Authorization"] = "";
            }
        }
    }
</script>