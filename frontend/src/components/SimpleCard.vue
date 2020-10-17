<template>

    <a href="#" @click="$emit('addCategory', dato)">
      <div>
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

div {
  vertical-align: center;
  height: 250px;
  width: 300px;
  text-align: center;
}
p{
  font-size: 50px;
}
a,div:hover{
  text-decoration: none;
  border-radius: 15px;
  color: #150485;
  background-color: rgba( 178, 222, 236,0.5);
}
</style>