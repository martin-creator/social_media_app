<template>
    <nav class="py-10 px-8 border-b border-gray-200">
            <div class="max-w-7xl mx-auto">
                <div class="flex items-center justify-between">
                    <div class="menu-left">
                        <a href="#" class="text-xl">Wey</a>
                    </div>

                    <div class="menu-right">
                        <a href="#" class="py-4 px-6 bg-gray-600 text-white rounded-lg">Log in</a>
                        <a href="#" class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</a>
                    </div>
                </div>
            </div>
        </nav>

        <main class="px-8 py-6 bg-gray-100">
            <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
                <div class="main-left col-span-2">
                    <div class="p-12 bg-white border border-gray-200 rounded-lg">
                        <h1 class="mb-6 text-2xl">Sign Up</h1>

                        <p class="mb-6 text-gray-500">
                            Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
                            Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
                        </p>

                        <p class="font-bold">
                            Already have an account? <RouterLink :to="{'name': 'login'}" class="underline">Click here</RouterLink> to login!
                        </p>
                    </div>
                </div>

                <div class="main-center col-span-2 space-y-4">
                    <div class="p-12 bg-white border border-gray-200 rounded-lg">
                        <form class="space-y-6">
                            <div>
                                <label>Name</label><br>
                                <input type="text" placeholder="Enter your fullname " class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                            </div>

                            <div>
                                <label>Email</label><br>
                                <input type="email" placeholder="Enter your email" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                            </div>

                            <div>
                                <label>Password</label><br>
                                <input type="password" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                            </div>

                            <div>
                                <label>Confirm Password</label><br>
                                <input type="password" placeholder="Confirm your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                            </div>

                            <div>
                                <button class="py-4 px-6 bg-purple-600 text-white rounded-lg"> Register</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </main>
</template>