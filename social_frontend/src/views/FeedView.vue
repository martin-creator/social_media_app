<template>
  <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 p-4">
    <div class="main-center md:col-span-3 space-y-4">
      <div class="bg-white border border-gray-200 rounded-lg p-4">
        <FeedForm v-bind:user="null" v-bind:posts="posts" />
      </div>

      <div class="space-y-4">
        <div
          class="bg-white border border-gray-200 rounded-lg p-4"
          v-for="post in posts"
          :key="post.id"
        >
          <FeedItem v-bind:post="post" v-on:deletePost="deletePost" />
        </div>
      </div>
    </div>

    <div class="main-right space-y-4">
      <div class="bg-white border border-gray-200 rounded-lg p-4">
        <PeopleYouMayKnow />
      </div>

      <div class="bg-white border border-gray-200 rounded-lg p-4">
        <Trends />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'
import FeedForm from '../components/FeedForm.vue'

export default {
    name: 'FeedView',

    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem,
        FeedForm
    },

    data() {
        return {
            posts: [],
            body: '',
        }
    },

    mounted() {
        this.getFeed()
    },

    methods: {
        getFeed() {
            axios
                .get('/api/posts/')
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        deletePost(id) {
            this.posts = this.posts.filter(post => post.id !== id)
        },
    }
}
</script>