
import threading
import speech_to_text as st


def start_thread(videos):
    import queue
    queue = queue.Queue()
    num = 0
    thread_lists = []
    output_from_api = {}
    output = []
    for i in videos:
        exec(fr'file = "videos\\{i}"')
        exec(f't{num} = threading.Thread(target = st.get_text, args = (file, num, queue))')
        exec(f't{num}.start()')
        exec(f'thread_lists.append(t{num})')

        num += 1

    for i in thread_lists:
        i.join()

    while not queue.empty():
        result = queue.get()
        output_from_api[result[1]] = result[0]

    for i in range(len(output_from_api)):
        output.append(output_from_api[i])
    return ' '.join(output)