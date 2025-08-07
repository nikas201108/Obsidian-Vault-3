#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <iomanip>
#include <sstream>
#include <filesystem>
#include <cstdlib>

namespace fs = std::filesystem;

std::string getCurrentTimestamp() {
    auto now = std::chrono::system_clock::now();
    auto time_t = std::chrono::system_clock::to_time_t(now);
    std::tm tm;
#ifdef _WIN32
    localtime_s(&tm, &time_t);  // Для Windows
#else
    tm = *std::localtime(&time_t);
#endif

    std::ostringstream oss;
    oss << std::put_time(&tm, "%Y-%m-%d_%H-%M-%S");
    return oss.str() + ".png";
}

int main() {
    std::string directory = "../Banners";  // Текущая директория

    try {
        if (!fs::exists(directory)) {
            std::cerr << "Директория не существует: " << directory << std::endl;
            return 1;
        }

        if (!fs::is_directory(directory)) {
            std::cerr << "Это не директория: " << directory << std::endl;
            return 1;
        }

        std::vector<fs::path> files;
        fs::path bannerPath = directory + "/banner.png";

        bool bannerExists = fs::exists(bannerPath) && fs::is_regular_file(bannerPath);

        for (const auto& entry : fs::directory_iterator(directory)) {
            if (entry.is_regular_file() && entry.path() != bannerPath) {
                files.push_back(entry.path());
            }
        }

        if (files.empty()) {
            std::cerr << "Нет файлов для выбора." << std::endl;
            return 1;
        }

        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<size_t> dist(0, files.size() - 1);
        fs::path selected = files[dist(gen)];

        if (bannerExists) {
            fs::path oldBannerNewName = directory + "/" + getCurrentTimestamp();
            fs::rename(bannerPath, oldBannerNewName);
            std::cout << "Старый banner.png переименован в: " << oldBannerNewName.filename().string() << std::endl;
        }

        fs::rename(selected, bannerPath);
        std::cout << "Файл '" << selected.filename().string() << "' стал banner.png" << std::endl;

    } catch (const std::exception& e) {
        std::cerr << "Ошибка: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}