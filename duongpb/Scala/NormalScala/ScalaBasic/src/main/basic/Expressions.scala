object Expressions extends App {
  val x = 1+2 //EXPRESSION

//  other math operator
// + - * / & | ^ << >> >>> 9 right shift with zero extension

println(!(1 == x))
//! && ||

var aVariable = 2
aVariable += 3 // -> 5

// Instruction & Expressions

//Instruction is what you tell the computer to do

//Expression is having a value or type ( VALUE ), this is more used in functional programming, when everything is returning a value

//example
val aCondition = true
val aConditionValue = if (aCondition) 5 else 3 // an If expression, because it gives back a value

// they have loop but not encourage to use
var i = 0

while (i < 10){
  println(i)
  i += 1
}
// DONT LOOP LIKE THIS since it's primitive

//EVERYTHING IN SCALA IS an EXPRESSION !

val aWeridValue = (aVariable = 3) // this data type is Unit === void in java, not returning anything meaningful

//reassigning a variables in scala create side effect == a unit
// side effect examples: print, whiles, reassigning, ...


// code blocks
val aCodeBlock = {
  val y = 2
  val z = y + 1

  if (z > 2) "hello" else "goodbye"
}
// the value of a block is the final value of the block
// everything you declare inside a code block cannot access outside the code block


}
