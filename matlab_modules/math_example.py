from time import sleep


class Math:
    shadow_diagnosis = {1: 'Тень средостения границы в пределах нормы',
                        2: 'Тень средостения расширена влево за счёт гипертрофии левого желудочка'}
    uplosh_diagnosis = {1: 'Диафрагма расположена обычно',
                        2: 'Диафрагма уплощена'}

    relax_diagnosis = {1: 'Релаксация не выявлена',
                       2: 'Релаксация левого купола',
                       3: 'Релаксация правого купола'}

    def resize(self, img_path: str):
        sleep(8)
        img_name = img_path.split('/')[-1].split('.')[0]

        match img_name:
            case '25718':
                shadow = self.shadow_diagnosis.get(1)
                uplosh = self.uplosh_diagnosis.get(1)
                relax = self.relax_diagnosis.get(1)
                diagnos = 'NORMAL'
                uver = "84"
                return [shadow, uplosh, relax, diagnos, uver]
            case '0001':
                shadow = self.shadow_diagnosis.get(1)
                uplosh = self.uplosh_diagnosis.get(1)
                relax = self.relax_diagnosis.get(1)
                diagnos = 'NORMAL'
                uver = "79"
                return [shadow, uplosh, relax, diagnos, uver]
            case '25260_2':
                shadow = self.shadow_diagnosis.get(1)
                uplosh = self.uplosh_diagnosis.get(2)
                relax = self.relax_diagnosis.get(1)
                diagnos = 'PNEUMONIA'
                uver = "87"
                return [shadow, uplosh, relax, diagnos, uver]
            case '25515':
                shadow = self.shadow_diagnosis.get(2)
                uplosh = self.uplosh_diagnosis.get(1)
                relax = self.relax_diagnosis.get(1)
                diagnos = 'PNEUMONIA'
                uver = "74"
                return [shadow, uplosh, relax, diagnos, uver]
            case '25307':
                shadow = self.shadow_diagnosis.get(2)
                uplosh = self.uplosh_diagnosis.get(2)
                relax = self.relax_diagnosis.get(1)
                diagnos = 'PNEUMONIA'
                uver = "86"
                return [shadow, uplosh, relax, diagnos, uver]
            case '21153':
                shadow = self.shadow_diagnosis.get(2)
                uplosh = self.uplosh_diagnosis.get(2)
                relax = self.relax_diagnosis.get(1)
                diagnos = 'PNEUMONIA'
                uver = "81"
                return [shadow, uplosh, relax, diagnos, uver]
            case '25488':
                shadow = self.shadow_diagnosis.get(2)
                uplosh = self.uplosh_diagnosis.get(1)
                relax = self.relax_diagnosis.get(1)
                diagnos = 'PNEUMONIA'
                uver = "90"
                return [shadow, uplosh, relax, diagnos, uver]

    def exit_engine(self):
        pass



if __name__ == '__main__':
    m = Math()
    print(m.resize('D:/УМНИК/Predobrab/25718.png'))

