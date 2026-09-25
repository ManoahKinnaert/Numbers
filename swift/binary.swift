import Foundation

enum Exceptions: Error {
    case IllegalArgumentError(String)
}

func decToBin(dec: Int) throws -> String {
    var dec = dec
    if dec < 0 { throw Exceptions.IllegalArgumentError("The integer dec must be positive!") }
    if dec == 0 { return "0" }
    var res = ""
    while dec > 0 {
        res = "\(dec % 2)\(res)"
        dec /= 2
    }
    return res     
}

func binToDec(bin: String) -> Int {
    var result = 0
    for (index, char) in bin.reversed().enumerated() {
        let bit = Int(char.wholeNumberValue ?? 0)
        result += bit * Int(pow(2, Double(index)))
    }
    return result
}

do {
    print(try decToBin(dec: 12))
    print(binToDec(bin: "1100"))
} catch {
    print(error)
}