import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from faker import Faker
import random
from datetime import datetime


class AdmissionDataGenerator:
    def __init__(self):
        self.fake = Faker('ru_RU')
        np.random.seed()
        random.seed()


        self.specialties = [
            'Прикладная информатика',
            'Экономика',
            'Медицина',
            'Строительство',
            'Психология',
            'Филология',
            'Математика',
            'Радиофизика',
            'Кибербезопастность'
        ]


        self.subjects = ['Математика', 'Русский язык', 'Физика', 'Химия', 'Биология', 'История', 'Иностранный язык']
        self.study_forms = ['Бюджет', 'Платная', 'Целевая']
        self.regions = ['Минск', 'Гродно', 'Брест', 'Витебск', 'Гомель', 'Могилев', 'Минская область']


        self.specialty_subjects = {
            'Прикладная информатика': ['Математика', 'Физика', 'Иностранный язык'],
            'Экономика': ['Математика', 'Русский язык', 'История'],
            'Медицина': ['Биология', 'Химия', 'Русский язык'],
            'Строительство': ['Математика', 'Физика', 'Русский язык'],
            'Психология': ['Биология', 'История', 'Русский язык'],
            'Филология': ['Русский язык', 'Иностранный язык', 'История'],
            'Математика': ['Математика', 'Физика', 'Иностранный язык'],
            'Радиофизика': ['Физика', 'Математика', 'Иностранный язык'],
            'Кибербезопастность': ['Математика', 'Физика', 'Русский язык']
        }

    def generate_student_data(self, year, num_students=1000):
        students = []

        for _ in range(num_students):
            full_name = self.fake.name()
            specialty = random.choice(self.specialties)
            study_form = random.choice(self.study_forms)
            address = f"{random.choice(self.regions)}, {self.fake.street_address()}"
            phone = self.fake.phone_number()


            certificate_score = round(np.random.normal(7.5, 1.2), 1)
            certificate_score = max(5.0, min(10.0, certificate_score))


            ct_scores = {}
            for subject in self.subjects:
                score = int(np.random.normal(65, 15))
                score = max(0, min(100, score))
                ct_scores[subject] = score


            main_subjects = self.specialty_subjects[specialty]
            total_ct_score = sum(ct_scores[subj] for subj in main_subjects)
            total_admission_score = total_ct_score + certificate_score * 10


            student_data = {
                'ФИО': full_name,
                'Год поступления': year,
                'Форма обучения': study_form,
                'Средний балл аттестата': certificate_score,
                'Общий балл при поступлении': total_admission_score,
                'Специальность': specialty,
                'Адрес регистрации': address,
                'Номер телефона': phone
            }

            student_data.update(ct_scores)
            students.append(student_data)

        return students

    def generate_5_years_data(self):

        all_data = []
        current_year = datetime.now().year
        years = list(range(current_year - 4, current_year + 1))

        for year in years:
            print(f"Генерация данных за {year} год...")
            yearly_data = self.generate_student_data(year)
            all_data.extend(yearly_data)

        return pd.DataFrame(all_data)


class DataVisualizer:
    def __init__(self, df):
        self.df = df

    def plot_ct_scores_dynamics(self):

        subjects = ['Математика', 'Русский язык', 'Физика', 'Химия', 'Биология', 'История', 'Иностранный язык']

        plt.figure(figsize=(14, 8))

        for subject in subjects:
            subject_data = self.df.groupby('Год поступления')[subject].mean()
            plt.plot(subject_data.index, subject_data.values, marker='o', linewidth=2, label=subject)

        plt.title('Динамика среднего балла за ЦТ/ЦЭ по предметам', fontsize=14, fontweight='bold')
        plt.xlabel('Год поступления')
        plt.ylabel('Средний балл')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def plot_certificate_scores_dynamics(self):

        plt.figure(figsize=(10, 6))

        cert_scores = self.df.groupby('Год поступления')['Средний балл аттестата'].mean()

        plt.plot(cert_scores.index, cert_scores.values, marker='s', linewidth=2,
                 markersize=8, color='red')
        plt.title('Динамика среднего балла аттестата', fontsize=14, fontweight='bold')
        plt.xlabel('Год поступления')
        plt.ylabel('Средний балл аттестата')
        plt.grid(True, alpha=0.3)

        for year, score in cert_scores.items():
            plt.annotate(f'{score:.2f}', (year, score), textcoords="offset points",
                         xytext=(0, 10), ha='center')

        plt.tight_layout()
        plt.show()

    def plot_passing_scores_dynamics(self):

        plt.figure(figsize=(12, 6))


        passing_scores = self.df.groupby(['Год поступления', 'Специальность'])[
            'Общий балл при поступлении'].min().unstack()

        passing_scores.plot(marker='o', linewidth=2, ax=plt.gca())
        plt.title('Динамика проходного балла по специальностям', fontsize=14, fontweight='bold')
        plt.xlabel('Год поступления')
        plt.ylabel('Проходной балл')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def plot_students_by_specialty(self):

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))


        specialty_counts = self.df['Специальность'].value_counts()

        ax1.bar(specialty_counts.index, specialty_counts.values, color='skyblue')
        ax1.set_title('Количество студентов по специальностям', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Специальность')
        ax1.set_ylabel('Количество студентов')
        plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')


        for i, count in enumerate(specialty_counts.values):
            ax1.text(i, count + 5, str(count), ha='center', va='bottom')


        yearly_specialty = pd.crosstab(self.df['Год поступления'], self.df['Специальность'])
        yearly_specialty.plot(kind='bar', ax=ax2, width=0.8)
        ax2.set_title('Количество студентов по специальностям по годам', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Год поступления')
        ax2.set_ylabel('Количество студентов')
        ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

        plt.tight_layout()
        plt.show()

    def plot_study_forms_statistics(self):

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))


        study_form_counts = self.df['Форма обучения'].value_counts()

        ax1.pie(study_form_counts.values, labels=study_form_counts.index, autopct='%1.1f%%',
                startangle=90, colors=['lightgreen', 'lightcoral', 'lightblue'])
        ax1.set_title('Распределение по формам обучения', fontsize=14, fontweight='bold')


        yearly_forms = pd.crosstab(self.df['Год поступления'], self.df['Форма обучения'])
        yearly_forms.plot(kind='bar', ax=ax2)
        ax2.set_title('Динамика форм обучения по годам', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Год поступления')
        ax2.set_ylabel('Количество студентов')
        ax2.legend(title='Форма обучения')

        plt.tight_layout()
        plt.show()


def main():

    print("Генерация данных о вступительной кампании за последние 5 лет...")


    generator = AdmissionDataGenerator()
    df = generator.generate_5_years_data()

    print(f"\nСгенерировано {len(df)} записей")
    print(f"Период: {df['Год поступления'].min()} - {df['Год поступления'].max()} годы")
    print(f"Количество специальностей: {len(df['Специальность'].unique())}")
    print(f"Формы обучения: {', '.join(df['Форма обучения'].unique())}")


    visualizer = DataVisualizer(df)

    print("\nСоздание визуализаций...")


    print("1. Динамика среднего балла за ЦТ/ЦЭ по предметам")
    visualizer.plot_ct_scores_dynamics()


    print("2. Динамика среднего балла аттестата")
    visualizer.plot_certificate_scores_dynamics()


    print("3. Динамика проходного балла")
    visualizer.plot_passing_scores_dynamics()


    print("4. Количество поступивших студентов по специальностям")
    visualizer.plot_students_by_specialty()


    print("5. Статистика по формам обучения")
    visualizer.plot_study_forms_statistics()


    df.to_csv('admission_campaign_data.csv', index=False, encoding='utf-8-sig')
    print(f"\nДанные сохранены в файл: admission_campaign_data.csv")

    # Вывод основной статистики
    print("\nОсновная статистика:")
    print(f"Средний балл аттестата: {df['Средний балл аттестата'].mean():.2f}")
    print(f"Средний общий балл при поступлении: {df['Общий балл при поступлении'].mean():.2f}")
    print(f"Самая популярная специальность: {df['Специальность'].mode().values[0]}")
    print(f"Самая распространенная форма обучения: {df['Форма обучения'].mode().values[0]}")


if __name__ == "__main__":
    main()