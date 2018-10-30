function isOddOrEven(_){
    return !`${_}`.match(/^\d+$/)||_%1?5:_.toString(2)
    .slice(-1)*1?"odd":"even"
}