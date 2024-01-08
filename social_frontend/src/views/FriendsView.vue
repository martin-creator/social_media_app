<template>
  <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-4 p-4">
    <div class="main-left col-span-1 md:col-span-1">
      <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
        <img
          :src="user.get_avatar"
          class="mb-6 mx-auto rounded-full max-w-full h-auto"
          alt="User Avatar"
        />
        <p class="text-lg font-semibold">{{ user.name }}</p>
        <div class="mt-2 flex flex-col space-y-2">
          <p class="text-xs text-gray-500">{{ user.friends_count }} friends</p>
          <p class="text-xs text-gray-500">{{ user.posts_count }} posts</p>
        </div>
      </div>
    </div>

    <div class="main-center col-span-1 md:col-span-2 space-y-4">
      <div
        class="p-4 bg-white border border-gray-200 rounded-lg"
        v-if="friendshipRequests.length"
      >
        <h2 class="mb-4 text-xl font-semibold">Friendship Requests</h2>

        <div
          class="p-4 bg-gray-100 border border-gray-200 rounded-lg mb-4"
          v-for="friendshipRequest in friendshipRequests"
          :key="friendshipRequest.id"
        >
          <img
            :src="friendshipRequest.created_by.get_avatar"
            class="mb-4 mx-auto rounded-full max-w-full h-auto"
            alt="Requester Avatar"
          />
          <p class="text-lg font-semibold">
            <RouterLink
              :to="{ name: 'profile', params: { id: friendshipRequest.created_by.id } }"
            >
              {{ friendshipRequest.created_by.name }}
            </RouterLink>
          </p>
          <div class="mt-2 flex flex-col space-y-2">
            <p class="text-xs text-gray-500">{{ user.friends_count }} friends</p>
            <p class="text-xs text-gray-500">{{ user.posts_count }} posts</p>
          </div>
          <div class="mt-4 flex space-x-4">
            <button
              @click="handleRequest('accepted', friendshipRequest.created_by.id)"
              class="inline-block py-2 px-4 bg-purple-600 text-white rounded-lg"
            >
              Accept
            </button>
            <button
              @click="handleRequest('rejected', friendshipRequest.created_by.id)"
              class="inline-block py-2 px-4 bg-red-600 text-white rounded-lg"
            >
              Reject
            </button>
          </div>
        </div>

        <hr class="my-4 border-t border-gray-300">
      </div>

      <div
        class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 gap-4"
        v-if="friends.length"
      >
        <div
          class="p-4 bg-gray-100 border border-gray-200 rounded-lg"
          v-for="friend in friends"
          :key="friend.id"
        >
          <img
            :src="friend.get_avatar"
            class="mb-4 mx-auto rounded-full max-w-full h-auto"
            alt="Friend Avatar"
          />
          <p class="text-lg font-semibold">
            <RouterLink :to="{ name: 'profile', params: { id: friend.id } }">
              {{ friend.name }}
            </RouterLink>
          </p>
          <div class="mt-2 flex flex-col space-y-2">
            <p class="text-xs text-gray-500">{{ friend.friends_count }} friends</p>
            <p class="text-xs text-gray-500">{{ friend.posts_count }} posts</p>
          </div>
        </div>
      </div>
    </div>

    <div class="main-right col-span-1 md:col-span-1 space-y-4">
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
import { useUserStore } from '@/stores/user'

export default {
    name: 'FriendsView',

    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    components: {
        PeopleYouMayKnow,
        Trends
    },

    data() {
        return {
            user: {},
            friendshipRequests: [],
            friends: []
        }
    },

    mounted() {
        this.getFriends()
    },

    methods: {
        getFriends() {
            axios
                .get(`/api/friends/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)

                    this.friendshipRequests = response.data.requests
                    this.friends = response.data.friends
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        handleRequest(status, pk) {
            console.log('handleRequest', status)

            axios
                .post(`/api/friends/${pk}/${status}/`)
                .then(response => {
                    console.log('data', response.data)
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>