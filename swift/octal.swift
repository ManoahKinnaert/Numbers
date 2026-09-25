import Foundation

enum Exceptions: Error {
    case IllegalArgumentError(String)
}

func decToOct(dec: Int) throws -> String {
    var dec = dec
    if dec < 0 { throw Exceptions.IllegalArgumentError("The integer dec must be positive!") }
    if dec == 0 { return "0" }
    var res = ""
    while dec > 0 {
        res = "\(dec % 8)\(res)"
        dec /= 8
    }
    return res     
}

func octToDec(oct: String) -> Int {
    var result = 0
    for (index, char) in oct.reversed().enumerated() {
        let part = Int(char.wholeNumberValue ?? 0)
        result += part * Int(pow(8, Double(index)))
    }
    return result
}

do {
    print(try decToOct(dec: 32))
    print(octToDec(oct: "234"))
} catch {
    print(error)
}