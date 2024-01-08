<template>
  <div class="max-w-7xl mx-auto p-4">
    <div class="main-left mb-4">
      <div class="p-6 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-4 text-3xl font-semibold">Sign up</h1>

        <p class="mb-4 text-gray-600">
          Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet.
          Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet.
        </p>

        <p class="font-bold">
          Already have an account?
          <RouterLink :to="{ name: 'login' }" class="text-purple-600 underline">
            Click here
          </RouterLink>
          to log in!
        </p>
      </div>
    </div>

    <div class="main-right">
      <div class="p-6 bg-white border border-gray-200 rounded-lg">
        <form class="space-y-4" v-on:submit.prevent="submitForm">
          <div>
            <label class="block text-lg font-semibold text-gray-800">Name</label>
            <input
              type="text"
              v-model="form.name"
              placeholder="Your full name"
              class="w-full mt-2 py-3 px-4 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500"
            />
          </div>

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
              v-model="form.password1"
              placeholder="Your password"
              class="w-full mt-2 py-3 px-4 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500"
            />
          </div>

          <div>
            <label class="block text-lg font-semibold text-gray-800">Repeat password</label>
            <input
              type="password"
              v-model="form.password2"
              placeholder="Repeat your password"
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
              Sign up
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

export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
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

            if (this.form.password1 === '') {
                this.errors.push('Your password is missing')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The password does not match')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'The user is registered. Please activate your account by clicking your email link.', 'bg-emerald-500')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            const data = JSON.parse(response.data.message)
                            for (const key in data){
                                this.errors.push(data[key][0].message)
                            }

                            this.toastStore.showToast(5000, 'Something went wrong. Please try again', 'bg-red-300')
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