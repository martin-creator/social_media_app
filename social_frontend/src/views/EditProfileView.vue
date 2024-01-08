<template>
  <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-4 p-4">
    <div class="main-left mb-4 md:mb-0">
      <div class="p-6 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-4 text-3xl font-semibold">Edit Profile</h1>

        <p class="mb-4 text-gray-600">
          Update your profile information and settings.
        </p>

        <RouterLink
          to="/profile/edit/password"
          class="text-purple-600 underline"
        >
          Edit Password
        </RouterLink>
      </div>
    </div>

    <div class="main-right">
      <div class="p-6 bg-white border border-gray-200 rounded-lg">
        <form class="space-y-6" @submit.prevent="submitForm">
          <div>
            <label for="name" class="block text-sm font-medium text-gray-600">
              Name
            </label>
            <input
              type="text"
              v-model="form.name"
              id="name"
              placeholder="Your full name"
              class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-purple-600"
            />
          </div>

          <div>
            <label
              for="email"
              class="block text-sm font-medium text-gray-600"
            >
              E-mail
            </label>
            <input
              type="email"
              v-model="form.email"
              id="email"
              placeholder="Your e-mail address"
              class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-purple-600"
            />
          </div>

          <div>
            <label
              for="avatar"
              class="block text-sm font-medium text-gray-600"
            >
              Avatar
            </label>
            <input
              type="file"
              ref="file"
              id="avatar"
              class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-purple-600"
            />
          </div>

          <template v-if="errors.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-4">
              <p v-for="error in errors" :key="error" class="text-sm">
                {{ error }}
              </p>
            </div>
          </template>

          <div>
            <button
              class="w-full py-2 px-4 bg-purple-600 text-white rounded-md hover:bg-purple-700 focus:outline-none focus:ring focus:border-purple-600"
            >
              Save Changes
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'

import { useToastStore } from '@/stores/toast'
import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const toastStore = useToastStore()
        const userStore = useUserStore()

        return {
            toastStore,
            userStore
        }
    },

    data() {
        return {
            form: {
                email: this.userStore.user.email,
                name: this.userStore.user.name
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.name === '') {
                this.errors.push('Your name is missing')
            }

            if (this.errors.length === 0) {
                let formData = new FormData()
                formData.append('avatar', this.$refs.file.files[0])
                formData.append('name', this.form.name)
                formData.append('email', this.form.email)

                axios
                    .post('/api/editprofile/', formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        }
                    })
                    .then(response => {
                        if (response.data.message === 'information updated') {
                            this.toastStore.showToast(5000, 'The information was saved', 'bg-emerald-500')

                            this.userStore.setUserInfo({
                                id: this.userStore.user.id,
                                name: this.form.name,
                                email: this.form.email,
                                avatar: response.data.user.get_avatar
                            })

                            this.$router.back()
                        } else {
                            this.toastStore.showToast(5000, `${response.data.message}. Please try again`, 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>