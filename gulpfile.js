var gulp = require('gulp'),
    gutil = require('gulp-util'),
    plumber = require('gulp-plumber')
    rename = require('gulp-rename'),
    prefix = require('gulp-autoprefixer'),
    minifycss = require('gulp-minify-css'), 
    uglify = require('gulp-uglify');

//Direcciones de Archivos: CSS's y JS's
var srcCSS = 'front-end/css/src/*.css',
    //distPrefix es el CSS con los prefijos de los navegadores
    distPrefix = 'front-end/css/prefix',
    distCSS = 'front-end/css/',
    srcJS = 'front-end/js/src/*.js', 
    distJS = 'front-end/js/';

//Task para los estilos CSS
gulp.task('styl', function(){
    gulp.src(srcCSS)
        .pipe(plumber())
        .pipe(prefix(['safari 5', 'ff 17', 'ie 10', 'opera 12.1', 'ios 5', 'android 2.2'])) //
        .pipe(gulp.dest(distPrefix))
        .pipe(minifycss())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(distCSS));
});

//Task para archivos Javascript
gulp.task('scripts', function(){
    gulp.src(srcJS)
        .pipe(plumber())
        .pipe(uglify())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(distJS));
});

//Task para supervisar cambios
gulp.task('watch', function(){
    gulp.watch(srcCSS, ['styl']);
    gulp.watch(srcJS, ['scripts']);
});

//Task default
//Se ejecuta con $ gulp
gulp.task('default',['styl', 'scripts', 'watch'], function(){
    console.log('Welcome to Ontomex FrontEnd!');
});