var gulp = require('gulp'),
    gutil = require('gulp-util'),
    plumber = require('gulp-plumber')
    rename = require('gulp-rename'),
    prefix = require('gulp-autoprefixer'),
    minifycss = require('gulp-minify-css'), 
    uglify = require('gulp-uglify');


var srcCSS = 'front-end/css/src/*.css',
    distCSS = 'front-end/css/',
    distPrefix = 'front-end/css/prefix',
    srcJS = 'front-end/js/src/*.js', 
    distJS = 'front-end/js/';

gulp.task('styl', function(){
    gulp.src(srcCSS)
        .pipe(plumber())
        .pipe(prefix(['safari 5', 'ff 17', 'ie 10', 'opera 12.1', 'ios 5', 'android 2.2'])) //
        .pipe(gulp.dest(distPrefix))
        .pipe(minifycss())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(distCSS));
});

gulp.task('scripts', function(){
    gulp.src(srcJS)
        .pipe(plumber())
        .pipe(uglify())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(distJS));
});

gulp.task('watch', function(){
    gulp.watch(srcCSS, ['styl']);
    gulp.watch(srcJS, ['scripts']);
});
gulp.task('default', function(){
    console.log('Welcome from PhyroServer!');
    gulp.watch(srcCSS, ['styl']);
    gulp.watch(srcJS, ['scripts']);
});