<template>
    <div>
        <div class="max-w-2xl mx-auto py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8">
            <div class="lg:grid lg:grid-cols-2 lg:gap-x-8 lg:items-start">
            <!-- Image gallery -->
            <div class="flex flex-col-reverse">
                <!-- Image selector -->
                

                <div class="w-full aspect-w-1 aspect-h-1">
                <!-- Tab panel, show/hide based on tab state. -->
                <div id="tabs-1-panel-1" aria-labelledby="tabs-1-tab-1" role="tabpanel" tabindex="0">
                    <img :src="product.get_image" alt="Angled front view with bag zipped and handles upright." class="w-full h-full object-center object-cover sm:rounded-lg">
                </div>

                <!-- More images... -->
                </div>
            </div>

            <!-- Product info -->
            <div class="mt-10 px-4 sm:px-0 sm:mt-16 lg:mt-0">
                <h1 class="text-3xl font-extrabold tracking-tight text-gray-900">{{product.name}}</h1>

                <div class="mt-3">
                <p class="text-3xl text-gray-900">${{product.price}}</p>
                </div>

                <div class="mt-6">
                <h3 class="sr-only">Description</h3>

                <div class="text-base text-gray-700 space-y-6">
                    <p>{{product.description}}</p>
                </div>
                </div>

                <div class="mt-6">
                    <div>
                        <input type="number" min="1" v-model="quantity">
                    </div>

                    <div @click="addToCart" type="submit" class="max-w-xs flex-1 bg-indigo-600 border border-transparent rounded-md py-3 px-8 flex items-center justify-center text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-50 focus:ring-indigo-500 sm:w-full">
                        Add to cart
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
    name: 'Product',
    data() {
        return {
            product: {},
            quantity: 1
        }
    },
    mounted() {
        this.getProduct()
    },
    methods: {
        getProduct() {
            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            axios
                .get(`/products/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },

        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart',item)
        }
    }
}
</script>