import {defineStore} from 'pinia'
import axios from 'axios'


export const useUserStore = defineStore({
    id: 'user',


    state: () => ({
        user : {
            isAuthenticated: false,
            id: null,
            name: null,
            email: null,
            access: null,
            refresh: null,
        }
    }),

    actions: {
        initStore() {
            if(localStorage.getItem('User.access')) {
                this.user.access = localStorage.getItem('User.access')
                this.user.refresh = localStorage.getItem('User.refresh')
                this.user.id = localStorage.getItem('User.id')
                this.user.name = localStorage.getItem('User.name')
                this.user.email = localStorage.getItem('User.email')
                this.user.isAuthenticated = true

                this.refreshToken()

                console.log('Initialized User', this.user)
                
                
            }
        },

        setToken(data){
            console.log('setToken', data)

            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            localStorage.setItem('User.access', data.access)
            localStorage.setItem('User.refresh', data.refresh)
        },

        removeToken(){
            console.log('removeToken')

            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = null
            this.user.name = null
            this.user.email = null

            localStorage.removeItem('User.access')
            localStorage.removeItem('User.refresh')
            localStorage.removeItem('User.id')
            localStorage.removeItem('User.name')
            localStorage.removeItem('User.email')
        },

        setUserInfo(user){
            console.log('setUserInfo', user)

            this.user.id = user.id
            this.user.name = user.name
            this.user.email = user.email

            localStorage.setItem('User.id', user.id)
            localStorage.setItem('User.name', user.name)
            localStorage.setItem('User.email', user.email)

            console.log('User', this.user)
        },

        refreshToken(){
            console.log('refreshToken')

            axios.post('api/refresh/', {
                refresh: this.user.refresh
            })
            .then((response) => {
                this.user.access = response.data.access
                localStorage.setItem('User.access', response.data.access)

                axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
            })
            .catch((error) => {
                console.log('refreshToken', error)

                this.removeToken()
            })
        }

    }
})



