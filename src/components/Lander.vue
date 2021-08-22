<template>
    <div>
        <div class="bio">
            <div class="vcenter">
                <img alt="Vue logo" class="rounded-circle" src="../assets/main.jpg" style="width:260px;height:260px;margin-bottom:1em">
                <h1 class="name">ROBERT LIANG</h1>
                <div class="bio-body">
                    MIT computer science graduate based in San Francisco.
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
</script>

<style lang="css" scoped>
    .bio {
        background-color: #0e232e;
        color: #efefef;
        height: 100vh;
        padding-left: 2em;
        padding-right: 2em;
    }

    .name {
        font-size: 48px;
        font-family: 'Lora';
        letter-spacing: 0.18em;
        padding-top: 0.5em;
    }
    .bio-body {
        border-top: 2px solid #4a90e2;
        padding-top: 1.2em;
        margin-top: 1.2em;
        position: relative;
        max-width: 480px;
        left: 50%;
        -moz-transform: translateX(-50%);
        -webkit-transform: translateX(-50%);
        transform: translateX(-50%);

    }
    .vcenter {
        position: relative;
        top: 50%;
        left: 50%;
        -moz-transform: translate(-50%,-50%);
        -webkit-transform: translate(-50%,-50%);
        transform: translate(-50%,-50%);
    }
</style>