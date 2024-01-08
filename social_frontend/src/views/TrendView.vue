<template>
  <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 p-4">
    <div class="main-center col-span-1 md:col-span-3 space-y-4">
      <div class="p-4 bg-white border border-gray-200 rounded-lg">
        <h2 class="text-2xl md:text-3xl lg:text-4xl font-bold">Trend: #{{ $route.params.id }}</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
        <div v-for="post in posts" :key="post.id">
          <div class="p-4 bg-white border border-gray-200 rounded-lg">
            <FeedItem :post="post" />
          </div>
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
    name: 'FeedView',

    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem
    },

    data() {
        return {
            posts: [],
        }
    },

    mounted() {
        this.getFeed()
    },

    watch: { 
        '$route.params.id': {
            handler: function() {
                this.getFeed()
            },
            deep: true,
            immediate: true
        }
    },

    methods: {
        getFeed() {
            axios
                .get(`/api/posts/?trend=${this.$route.params.id}`)
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    }
}
</script>