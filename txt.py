# команды гита
# git init -> создает репозиторий.
# git status -> показывает информацию о статусе проекта в git.
# git commit -m '' -> закоммитить изменения в локальной репозиторий.


# git add .
# git remote add origin https://github.com/stanruss/название.git
# git push -u origin master
#
# git log --oneline - посмотреть все коммиты.
# git checkout . - восстановить все.
# git checkout "код коммита" - вернуть до состояния этого коммита.
# git checkout master - вернуться в ветку мастер.

#
# git add text.txt - Добавить файл в репозиторий
# git rm text.txt - Удалить файл
# git status - Текущее состояние репозитория (изменения, неразрешенные конфликты и тп)
# git commit -a -m "Commit description" - Сделать коммит

# git push origin master - Аналогично предыдущему, но делается пуш только ветки master
# git push origin HEAD - Запушить текущую ветку, не вводя целиком ее название
# git checkout -b some_branch origin/some_branch - Начать работать с веткой some_branch (уже существующей)
# git branch some_branch - Создать новый бранч (ответвится от текущего)
# git checkout some_branch - Переключиться на другую ветку (из тех, с которыми уже работаем)

# git branch -d some_branch - Удалить бранч (после мерджа)
# git branch -D some_branch - Просто удалить бранч
# git push origin :branch-name - Удалить бранч из репозитория на сервере


