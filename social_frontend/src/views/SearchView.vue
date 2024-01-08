<template>
  <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 p-4">
    <div class="main-left col-span-1 md:col-span-2 lg:col-span-3 space-y-4">
      <div class="bg-white border border-gray-200 rounded-lg p-4">
        <form @submit.prevent="submitForm" class="flex flex-col md:flex-row md:space-x-4">
          <input v-model="query" type="search" class="p-4 w-full md:w-2/3 bg-gray-100 rounded-lg" placeholder="What are you looking for?" />

          <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"></path>
            </svg>
          </button>
        </form>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div v-if="users.length">
          <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="user in users" :key="user.id">
            <img :src="user.get_avatar" class="mb-6 rounded-full">

            <p class="mb-2">
              <strong>
                <RouterLink :to="{ name: 'profile', params: { 'id': user.id } }">{{ user.name }}</RouterLink>
              </strong>
            </p>

            <div class="flex space-x-2 text-xs text-gray-500">
              <p>{{ user.friends_count }} friends</p>
              <p>{{ user.posts_count }} posts</p>
            </div>
          </div>
        </div>

        <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in posts" :key="post.id">
          <FeedItem :post="post" />
        </div>
      </div>
    </div>

    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />

      <Trends />
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'

export default {
    name: 'SearchView',

    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem,
    },

    data() {
        return {
            query: '',
            users: [],
            posts: []
        }
    },

    methods: {
        submitForm() {
            console.log('submitForm', this.query)

            axios
                .post('/api/search/', {
                    query: this.query
                })
                .then(response => {
                    console.log('response:', response.data)

                    this.users = response.data.users
                    this.posts = response.data.posts
                })
                .catch(error => {
                    console.log('error:', error)
                })
        }
    }
}
</script>