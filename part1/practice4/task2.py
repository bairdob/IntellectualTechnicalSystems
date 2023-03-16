from git import Repo


def read_file(path: str) -> list:
    with open(path) as f:
        data = f.readlines()
    return data


def cloning_repo(url: str, folder: str):
    """
    клонирует репозиторий по ссылке в папку
    """
    try:
        print('cloning {}... into {}'.format(url, folder))
        Repo.clone_from(url, folder)
    except Exception as e:
        pass

def logging(url: str):
    """
    логирует результаты клонирования 
    """
    if Repo(git_url):
        with open(log_file, 'a') as f:
            f.write(git_url + ' OK\n')
    # TODO git.exc.NoSuchPathError
    else:
        with open(log_file, 'a') as f:
            f.write(git_url + ' FAIL\n')


if __name__ == '__main__':
    log_file = 'git.log'
    gits = read_file('git.txt')

    for git in gits:
        # получаем ссылку репозитория и имя папки (куда клонировать)
        git_url = git.rstrip()
        folder = git.rstrip().split('/')[-1] + '-ssh'

        cloning_repo(git_url, folder)
        logging(git_url)

