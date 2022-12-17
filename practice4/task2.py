from git import Repo


def read_file(path: str) -> list:
    with open(path) as f:
        data = f.readlines()
    return data


if __name__ == '__main__':
    log_file = 'git.log'
    gits = read_file('git.txt')

    for git in gits:
        # получаем ссылку репозитория и имя папки (куда клонировать)
        git = git.rstrip()
        name = git.rstrip().split('/')[-1] + '-ssh'

        try:
            # clone via ssh (will use default keys)
            print('cloning {}... into {}'.format(git,name))
            result = Repo.clone_from(git, name) 
            print(result)
        except Exception as e:
            # pass
            print(e)
            
        # логируем результаты клонирования
        if Repo(name):
            with open(log_file, 'a') as f:
                f.write(name + ' OK\n')
        # TODO git.exc.NoSuchPathError 
        else:
            with open(log_file, 'a') as f:
                f.write(name + ' FAIL\n')

        # try:
        #     Repo(name)
        #     with open(log_file, 'a') as f:
        #         f.write(name + ' OK\n')
        # # TODO git.exc.NoSuchPathError 
        # except NoSuchPathError:
        #     with open(log_file, 'a') as f:
        #         f.write(name + ' FAIL\n')
        

