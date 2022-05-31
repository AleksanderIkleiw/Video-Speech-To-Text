
## Function Reference

#### Mp4 to Text

```http
  work(filename)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `filename` | `string` | Self explainatory |

In order to change desired language recognition, you need to head over to `speech_to_text.py` and change `    queue.put([r.recognize_google(audio, language="pl-PL"), num_of_operation])`
`language` parameter for ex. to `"en-EN"`
The application uses google's API and sends multiple requests with sliced audio in order to be able to convert speech to text.
