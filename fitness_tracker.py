from message import InfoMessage
from training import Running, SportsWalking, Swimming, Training


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    train = {"SWM": Swimming, "RUN": Running, "WLK": SportsWalking}
    if workout_type not in train:
        raise KeyError("Неверно указан код тренировки")
    return train[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == "__main__":
    packages = [
        ("SWM", [720, 1, 80, 25, 40]),
        ("RUN", [15000, 1, 75]),
        ("WLK", [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
