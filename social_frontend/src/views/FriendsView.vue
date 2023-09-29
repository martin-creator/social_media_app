<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
      <div class="main-left col-span-1">
        <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
          <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full" />
  
          <p><strong>{{ user.name }}</strong></p>
  
          <div class="mt-6 flex space-x-8 justify-around">
            <p class="text-xs text-gray-500">182 friends</p>
            <p class="text-xs text-gray-500">120 posts</p>
          </div>
        </div>
      </div>
  
      <div class="main-center col-span-2 space-y-4">
       Frindsssssssssssssss
      </div>
  
      <div class="main-right col-span-1 space-y-4">
        <div class="p-4 bg-white border border-gray-200 rounded-lg">
          <h3 class="mb-6 text-xl">People you may know</h3>
          <PeopleYouMayKnow />
        </div>
  
        <div class="p-4 bg-white border border-gray-200 rounded-lg">
          <h3 class="mb-6 text-xl">Trends</h3>
          <Trends />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
  import Trends from "../components/Trends.vue";
  import {useUserStore} from "@/stores/user";
  import FeedItem from "@/components/FeedItem.vue";
  
  export default {
    name: "FriendsView",
    setup() {
    const userStore = useUserStore();

    return {
      userStore,
    };
  },

    components: {
      PeopleYouMayKnow,
      Trends,
      
    },
  
    data() {
      return {
      };
    },
  
    mounted() {
    },

  
    methods: {
      
    },
  };
  </script>
  