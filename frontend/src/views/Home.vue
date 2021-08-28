<template>
  <div class="">
    <div class="max-w-2xl mx-auto py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8">
      <div class="mt-12 max-w-lg mx-auto grid gap-5 lg:grid-cols-3 lg:max-w-none">

          <div v-for="product in Products" :key="product.id" class="flex flex-col overflow-hidden">

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
// @ is an alias to /src
import { getAPI } from '../axios-api'

export default {
  name: 'Products',
  data () {
    return {
      Products: []
    }
  },
  created () {
        getAPI.get('/products/list/',)
          .then(response => {
            console.log('Post API has recieved data')
            this.Products = response.data
          })
          .catch(err => {
            console.log(err)
          })
    }
}
</script>
