<template>
    <div>
        <section class="about">
            <h1>About me</h1>
            <div class="about-body py-4">
                Hi! I'm <strong>Robert</strong>. I love learning new things.
                <br><br>
                Right now I'm a <strong>Member of Technical Staff</strong> at <strong>Cerebras Systems</strong>.
                I graduated from <strong>MIT</strong> with a Master's and Bachelor's in electrical engineering and computer science.
                In the past I've also worked as a quantitative researcher at <strong>Sandia Point Capital</strong>, graduate student at MIT's <strong>Center for Brains, Minds, and Machines</strong>, and software engineering intern at <strong>Google</strong>.
                <br><br>
                <h3>I like...</h3>
                ...software that's well designed and serves a good purpose
                <br><br>
                ...machine learning, especially for understanding human languages (NLP) and behavior (recommender systems)
                <br><br>
                ...cutting edge research that pushes the limits of science and engineering
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
                ...try to learn Cantonese
            </div>
        </section>
    </div>
</template>


<style lang="css" scoped>
    .about{
        background-color: #34345238;
        padding-top: 8%;
        padding-bottom: 5%;
        padding-left: 2em;
        padding-right: 2em;
    }

    .about-body {
        position: relative;
        max-width: 600px;
        left: 50%;
        -moz-transform: translateX(-50%);
        -webkit-transform: translateX(-50%);
        transform: translateX(-50%);
        text-align: left;
    }
</style>