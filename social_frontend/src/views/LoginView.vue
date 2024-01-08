<template>
  <div class="max-w-7xl mx-auto md:grid md:grid-cols-2 md:gap-4 p-4">
    <div class="md:col-span-1">
      <div class="p-6 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-6 text-3xl md:text-4xl font-bold">Log in</h1>

        <p class="mb-6 text-gray-600">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>

          <p class="mb-6 text-gray-600">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p><br/><br/>


        <p class="text-gray-800 font-semibold">
          Don't have an account?
          <RouterLink :to="{ name: 'signup' }" class="text-purple-600 hover:underline">
            Click here
          </RouterLink>
          to create one!
        </p>
      </div>
    </div>

    <div class="md:col-span-1 mt-4 md:mt-0">
      <div class="p-6 bg-white border border-gray-200 rounded-lg">
        <form class="space-y-6" v-on:submit.prevent="submitForm">
          <div>
            <label class="block text-lg font-semibold text-gray-800">E-mail</label>
            <input
              type="email"
              v-model="form.email"
              placeholder="Your e-mail address"
              class="w-full mt-2 py-3 px-4 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500"
            />
          </div>

          <div>
            <label class="block text-lg font-semibold text-gray-800">Password</label>
            <input
              type="password"
              v-model="form.password"
              placeholder="Your password"
              class="w-full mt-2 py-3 px-4 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500"
            />
          </div>

          <template v-if="errors.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-4">
              <p v-for="error in errors" :key="error" class="text-sm">{{ error }}</p>
            </div>
          </template>

          <div>
            <button class="py-3 px-4 bg-purple-600 text-white rounded-lg hover:bg-purple-700 focus:outline-none">
              Log in
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'

import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                password: '',
            },
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.password === '') {
                this.errors.push('Your password is missing')
            }

            if (this.errors.length === 0) {
                await axios
                    .post('/api/login/', this.form)
                    .then(response => {
                        this.userStore.setToken(response.data)

                        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    })
                    .catch(error => {
                        console.log('error', error)

                        this.errors.push('The email or password is incorrect! Or the user is not activated!')
                    })
            }
            
            if (this.errors.length === 0) {
                await axios
                    .get('/api/me/')
                    .then(response => {
                        this.userStore.setUserInfo(response.data)

                        this.$router.push('/feed')
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>