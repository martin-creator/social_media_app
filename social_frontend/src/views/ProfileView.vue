<template>
  <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 p-4">
    <div class="main-left md:col-span-1">
      <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
        <img :src="user.get_avatar" class="mb-6 rounded-full">

        <p class="text-lg font-semibold">{{ user.name }}</p>

        <div class="mt-2 flex space-x-4 text-gray-500 text-sm">
          <RouterLink
            :to="{ name: 'friends', params: { id: user.id } }"
            class="flex items-center"
          >
            <span>{{ user.friends_count }}</span>
            <span class="ml-1">Friends</span>
          </RouterLink>
          <span class="flex items-center">
            {{ user.posts_count }}
            <span class="ml-1">Posts</span>
          </span>
        </div>

        <div class="mt-6 space-y-2">
          <button
            v-if="userStore.user.id !== user.id && can_send_friendship_request"
            class="block w-full py-2 bg-purple-600 text-white rounded-md"
            @click="sendFriendshipRequest"
          >
            Send Friendship Request
          </button>
          <button
            v-if="userStore.user.id !== user.id"
            class="block w-full py-2 bg-purple-600 text-white rounded-md"
            @click="sendDirectMessage"
          >
            Send Direct Message
          </button>
          <RouterLink
            v-if="userStore.user.id === user.id"
            class="block w-full py-2 bg-purple-600 text-white rounded-md"
            to="/profile/edit"
          >
            Edit Profile
          </RouterLink>
          <button
            v-if="userStore.user.id === user.id"
            class="block w-full py-2 bg-red-600 text-white rounded-md"
            @click="logout"
          >
            Log Out
          </button>
        </div>
      </div>
    </div>

    <div class="main-center md:col-span-2 space-y-4">
      <div
        v-if="userStore.user.id === user.id"
        class="bg-white border border-gray-200 rounded-lg p-4"
      >
        <FeedForm v-bind:user="user" v-bind:posts="posts" />
      </div>

      <div
        v-for="post in posts"
        :key="post.id"
        class="p-4 bg-white border border-gray-200 rounded-lg"
      >
        <FeedItem v-bind:post="post" v-on:deletePost="deletePost" />
      </div>
    </div>

    <div class="main-right md:col-span-1 space-y-4">
      <div class="bg-white border border-gray-200 rounded-lg p-4">
        <PeopleYouMayKnow />
      </div>

      <div class="bg-white border border-gray-200 rounded-lg p-4">
        <Trends />
      </div>
    </div>
  </div>
</template>


<style>
input[type="file"] {
    display: none;
}

.custom-file-upload {
    border: 1px solid #ccc;
    display: inline-block;
    padding: 6px 12px;
    cursor: pointer;
}
</style>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'
import FeedForm from '../components/FeedForm.vue'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    name: 'FeedView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },

    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem,
        FeedForm
    },

    data() {
        return {
            posts: [],
            user: {
                id: ''
            },
            can_send_friendship_request: null,
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
        deletePost(id) {
            this.posts = this.posts.filter(post => post.id !== id)
        },

        sendDirectMessage() {
            console.log('sendDirectMessage')

            axios
                .get(`/api/chat/${this.$route.params.id}/get-or-create/`)
                .then(response => {
                    console.log(response.data)

                    this.$router.push('/chat')
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        sendFriendshipRequest() {
            axios
                .post(`/api/friends/${this.$route.params.id}/request/`)
                .then(response => {
                    console.log('data', response.data)

                    this.can_send_friendship_request = false

                    if (response.data.message == 'request already sent') {
                        this.toastStore.showToast(5000, 'The request has already been sent!', 'bg-red-300')
                    } else {
                        this.toastStore.showToast(5000, 'The request was sent!', 'bg-emerald-300')
                    }
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        getFeed() {
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data.posts
                    this.user = response.data.user
                    this.can_send_friendship_request = response.data.can_send_friendship_request
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        logout() {
            console.log('Log out')

            this.userStore.removeToken()

            this.$router.push('/login')
        }
    }
}
</script>