<template>
    <div>
        <section class="bio">
            <div class="vcenter">
                <img alt="Vue logo" class="rounded-circle" src="../assets/main.jpg" style="width:220px;height:220px;margin-bottom:2em">
                <h1>Robert Liang</h1> 
                <div class="bio-body">
                    MIT computer science graduate based in San Francisco.
                </div>
            </div>
        </section>
    </div>
</template>

<script lang="ts">
</script>

<style lang="css" scoped>
    .bio{
        background-color: #0e232e;
        color: #efefef;
        height: 100vh;
    }

    .bio-body {
        border-top: 2px solid #4a90e2;
        padding-top: 1em;
        margin-top: 1em;
        position: relative;
        width: 480px;
        left: 50%;
        -moz-transform: translateX(-50%);
        -webkit-transform: translateX(-50%);
        transform: translateX(-50%);

    }
    .vcenter{
        position: relative;
        top: 50%;
        left: 50%;
        -moz-transform: translate(-50%,-50%);
        -webkit-transform: translate(-50%,-50%);
        transform: translate(-50%,-50%);
    }
</style>