<template>

    <a href="#" @click="$emit('addCategory', dato) " id="catCard" class="tarjeta-cat">
      <div >
        <p >{{dato}}</p>
        <img :src=generateUrl(dato) alt="" style="height: 150px;width: 100px">
      </div>
    </a>

</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "SimpleCard",

  computed:{
    ...mapGetters["roomCategories"]
  },

  props: {dato:String},

  methods:{
    generateUrl(name){
      return "Images/Categories/"+ name+".png"
    },
  },
}
</script>

<style scoped>


p{
  font-size: 25px;
}
a,div:hover{
  text-decoration: none;
}
</style>