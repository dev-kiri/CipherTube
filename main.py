from ciphertube import CipherTube

if __name__ == '__main__':
    print('Type youtube url to download')
    url = input('>> ')
    ciphertube = CipherTube(url)
    print(ciphertube.title)
    print('\n'.join([str(x) for x in ciphertube.streams]))
    print('Now, type the itag which you want to download from these streams.')
    itag = int(input('>> '))
    ciphertube.stream(itag=itag).download()