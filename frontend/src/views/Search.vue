<template >
    <div class="relative bg-gray-50 pt-16 pb-20 px-4 sm:px-6 lg:pt-24 lg:pb-28 lg:px-8">
  <div class="absolute inset-0">
    <div class="bg-white h-1/3 sm:h-2/3"></div>
  </div>
  <div class="relative max-w-7xl mx-auto">
    <div class="text-center">
      <h2 class="text-3xl tracking-tight font-extrabold text-gray-900 sm:text-4xl">
        Search results
      </h2>
      <p class="mt-3 max-w-2xl mx-auto text-xl text-gray-500 sm:mt-4">
        You searched: {{ query }}
      </p>
    </div>
    <div class="mt-12 max-w-lg mx-auto grid gap-5 lg:grid-cols-3 lg:max-w-none">

        <div v-for="product in products" :key="product.id" class="flex flex-col overflow-hidden">

            <div class="group relative">
              <div class="w-full min-h-80 bg-gray-200 aspect-w-1 aspect-h-1 rounded-md overflow-hidden group-hover:opacity-75 lg:h-80 lg:aspect-none">
                <img :src="product.get_image" alt="Front of men&#039;s Basic Tee in black." class="w-full h-full object-center object-cover lg:w-full lg:h-full">
              </div>
              <div class="mt-4 flex justify-between">
                <div>
                  <h3 class="text-sm text-gray-700">
                    <router-link v-bind:to="product.get_absolute_url">
                      <span aria-hidden="true" class="absolute inset-0"></span>
                      {{product.name}}
                    </router-link>
                  </h3>
                </div>
                <p class="text-sm font-medium text-gray-900">$ {{ product.price }}</p>
              </div>
            </div>
        </div>

    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name:"Search",
    data(){
        return {
            products: [],
            query: ''
        }
    },
    mounted(){
        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')){
            this.query = params.get('query')
            this.performSearch()
        }
    },
    methods: {
        performSearch(){
            axios
                .post('/products/search/', {'query': this.query})
                .then(response => {
                    this.products = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>