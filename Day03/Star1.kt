import java.io.File
import java.io.InputStream

fun main() {
    val inputStream: InputStream = File("data.txt").inputStream();
    val lineList = mutableListOf<String>();
    inputStream.bufferedReader().forEachLine { lineList.add(it) }
    var gamma = IntArray(lineList.first().length);
    var epsilon = IntArray(lineList.first().length);
    lineList.forEach{
      for(i in it.indices){
          val value : Int = (it[i].code - '0'.code);
          gamma[i] += value;
          epsilon[i] += if(value==1) 0 else 1;
      }
    }
    gamma = transform(gamma, lineList.size/2);
    val gamma_res : Int = toInt(gamma);
    epsilon = transform(epsilon, lineList.size/2);
    val epsilon_res : Int = toInt(epsilon);

    println(gamma_res);
    println(epsilon_res);
    println(gamma_res*epsilon_res);
}

fun transform(value: IntArray, comp: Int) : IntArray {
    for (i in value.indices){
      value[i] = if(value[i] > comp) 1 else 0;
    }
    return value;
}

fun toInt(value: IntArray) : Int {
    var res : Int = 0;
    val reversed_value : IntArray = value.reversedArray();
    for (i in reversed_value.indices){
      res += reversed_value[i]*(Math.pow(2.toDouble(), i.toDouble()).toInt());
    }
    return res;
}
