<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-1">
      <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
        <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full" />

        <p>
          <strong>{{ user.name }}</strong>
        </p>

        <div class="mt-6 flex space-x-8 justify-around">
          <p class="text-xs text-gray-500">182 friends</p>
          <p class="text-xs text-gray-500">120 posts</p>
        </div>
      </div>
    </div>

    <div class="main-center col-span-2 space-y-4 mb-4">
      <div
        class="p-4 bg-white border border-gray-200 rounded-lg"
        v-if="friendshipRequests.length"
      >
        <h2 class="mb-6 text-xl">Friendship requests</h2>
        <div
          class="p-4 text-center bg-white-100 rounded-lg"
          v-for="friendshipRequest in friendshipRequests"
          v-bind:key="friendshipRequest.id"
        >
          <img
            src="https://i.pravatar.cc/100?img=70"
            class="mb-6 mx-auto rounded-full"
          />

          <p>
            <strong>
              <RouterLink
                :to="{
                  name: 'profile',
                  params: { id: friendshipRequest.created_by.id },
                }"
                >{{ friendshipRequest.created_by.name }}</RouterLink
              >
            </strong>
          </p>

          <div class="mt-6 flex space-x-8 justify-around">
            <!-- <p class="text-xs text-gray-500">{{ user.friends_count }} friends</p>
                        <p class="text-xs text-gray-500">{{ user.posts_count }} posts</p> -->
            <p class="text-xs text-gray-500">182 friends</p>
            <p class="text-xs text-gray-500">120 posts</p>
          </div>

          <div class="mt-6 space-x-4">
            <button
              class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg"
              @click="
                handleRequest('accepted', friendshipRequest.created_by.id)
              "
            >
              Accept
            </button>
            <button
              class="inline-block py-4 px-6 bg-red-600 text-white rounded-lg"
              @click="
                handleRequest('rejected', friendshipRequest.created_by.id)
              "
            >
              Reject
            </button>
          </div>
        </div>
      </div>
      <hr />
      <div
      class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-2 gap-4"
      v-if="friends.length"
    >
      <div
        class="p-4 text-center bg-gray-100 rounded-lg"
        v-for="user in friends"
        v-bind:key="user.id"
      >
        <img src="https://i.pravatar.cc/100?img=70" class="mb-6 rounded-full text-center" />

        <p>
          <strong>
            <RouterLink :to="{ name: 'profile', params: { id: user.id } }">{{
              user.name
            }}</RouterLink>
          </strong>
        </p>

        <div class="mt-6 flex space-x-8 justify-around">
          <p class="text-xs text-gray-500">{{ user.friends_count }} friends</p>
          <p class="text-xs text-gray-500"> 5 posts</p>
        </div>
      </div>
    </div>
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
import { useUserStore } from "@/stores/user";

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
      user: {},
      friendshipRequests: [],
      friends: [],
    };
  },

  mounted() {
    this.getFriends();
  },

  methods: {
    getFriends() {
      console.log("Getting feed");
      axios
        .get(`/api/friends/${this.$route.params.id}/`)
        .then((response) => {
          this.friendshipRequests = response.data.requests;
          this.friends = response.data.friends;
          this.user = response.data.user;
          console.log(response.data);
        })
        .catch((error) => {
          console.log("Error: ", error);
        });
    },

    handleRequest(status, pk) {
      axios
        .post(`/api/friends/${pk}/${status}/`)
        .then((response) => {
          //this.getFriends();
          console.log(response.data);
        })
        .catch((error) => {
          console.log("Error: ", error);
        });
    },
  },
};
</script>