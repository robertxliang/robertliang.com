<template>
    <div>
        <section class="about">
            <h1>About me</h1>
            <div class="about-body py-4">
                Hi! I'm <strong>Robert</strong>. I love learning new things.
                <br><br>
                Right now I'm a <strong>Member of Technical Staff</strong> at <strong>Cerebras Systems</strong>.
                I graduated from <strong>MIT</strong> with a Master's and Bachelor's in electrical engineering and computer science.
                In the past I've also worked as a quantitative researcher at <strong>Sandia Point Capital</strong>, as a graduate student at MIT's <strong>Center for Brains, Minds, and Machines</strong>, and as a software engineering intern at <strong>Google</strong>.
                <br><br>
                <h3>I love...</h3>
                ...writing software that's well designed and serves a good purpose
                <br><br>
                ...studying and applying machine learning, especially when used for understanding human languages (natural language processing) and behavior (recommender systems)
                <br><br>
                ...learning and teaching all sorts of things
                <br><br>
                <h3>In my spare time, I like to...</h3>
                ...climb at Planet Granite
                <br><br>
                ...build things
                <br><br>
                ...explore California's diverse natural scenery
                <br><br>
                <h3>I also like to...</h3>
                ...listen to Chinese and Korean pop music
                <br><br>
                ...try new restaurants from Eater and recipes from NYTimes Cooking
                <br><br>
                ...learn and practice Cantonese
            </div>
        </section>
    </div>
</template>


<style lang="css" scoped>
    .about {
        background-color: #34345238;
        padding-top: 4em;
        padding-bottom: 3em;
        padding-left: 2em;
        padding-right: 2em;
    }

    .about-body {
        position: relative;
        max-width: 550px;
        left: 50%;
        -moz-transform: translateX(-50%);
        -webkit-transform: translateX(-50%);
        transform: translateX(-50%);
        text-align: left;
    }
</style>