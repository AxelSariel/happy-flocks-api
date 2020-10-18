var query = "#UltraHacks"
var apiUrl = "http://35.192.117.152:5000/api/v1/tweets/happytest"
var completeUrl = apiUrl + "?q=" + query
let url = URL(completeUrl)

let task = URLSession.shared.dataTask(with: url) {(data, response, error)
    guard let data = data else { return }
    print(String(data: data, encoding: .utf8)!)
}

task.resume()

