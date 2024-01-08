<template>
  <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4">
    <div class="main-center col-span-1 md:col-span-2 lg:col-span-3 space-y-4">
      <div
        class="p-4 bg-white border border-gray-200 rounded-lg"
        v-for="notification in notifications"
        :key="notification.id"
        v-if="notifications.length"
      >
        <p class="text-gray-700">{{ notification.body }}</p>

        <button
          class="text-purple-600 underline mt-2 inline-block"
          @click="readNotification(notification)"
        >
          Read more
        </button>
      </div>

      <div
        class="p-4 bg-white border border-gray-200 rounded-lg text-center"
        v-else
      >
        You don't have any unread notifications!
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'

export default {
    name: 'notifications',

    data() {
        return {
            notifications: []
        }
    },

    mounted() {
        this.getNotifications()
    },

    methods: {
        getNotifications() {
            axios
                .get('/api/notifications/')
                .then(response => {
                    console.log(response.data)

                    this.notifications = response.data
                })
                .catch(error => {
                    console.log('Error: ', error)
                })
        },

        async readNotification(notification) {
            console.log('readNotification', notification.id)

            await axios
                .post(`/api/notifications/read/${notification.id}/`)
                .then(response => {
                    console.log(response.data)

                    if (notification.type_of_notification == 'post_like' || notification.type_of_notification == 'post_comment') {
                        this.$router.push({name: 'postview', params: {id: notification.post_id}})
                    } else {
                        this.$router.push({name: 'friends', params: {id: notification.created_for_id}})
                    }
                })
                .catch(error => {
                    console.log('Error: ', error)
                })
        }
    }
}
</script>